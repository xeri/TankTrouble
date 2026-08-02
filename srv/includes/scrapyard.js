var Scrapyard = Scrapyard || {};

Scrapyard.UIConstants = {
	SCRAPYARD_PLATE_WIDTH: 11,					// canvas px 
	SCRAPYARD_PLATE_HEIGHT: 22,					// canvas px
	SCRAPYARD_PLATE_SPACING: 1,					// canvas px
	SCRAPYARD_FLIP_DELAY: 100,					// ms - delay between spawning and flipping plates 
	SCRAPYARD_FLIP_TIME: 630,					// ms - time it takes to flip a plate
	SCRAPYARD_FIRST_UPDATE: 60000,				// ms - time to first update
	SCRAPYARD_FOLLOWING_UPDATES: 300000     	// ms - time between following updates    
}

Scrapyard.UIPlateImage = function(game) {
    
	// Call super.
    Phaser.Image.call(this, game, 0, 0, 'plates');
    
	// State
	this.ancestor = null;
	this.created = 0;
	this.digit = 0;
	
    // Disable plate
    this.kill();
}

Scrapyard.UIPlateImage.prototype = Object.create(Phaser.Image.prototype);
Scrapyard.UIPlateImage.prototype.constructor = Scrapyard.UIPlateImage;

Scrapyard.UIPlateImage.prototype.spawn = function(x, y, digit, flipped, ancestor) {

    // Revive and place the sprite
    this.reset(x, y);
	
	// State
	this.ancestor = ancestor;
	this.created = this.game.time.now;
	this.digit = digit;

	// Set up plate
	if (flipped) {
		this.frame = this.digit + 10;
		this.bringToTop();	
	} else {
		this.anchor.y = 1;
		this.frame = this.digit;
		this.sendToBack();
	}
}

Scrapyard.UIPlateImage.prototype.flip = function() {
	
	// Begin flip tween
	var topTween = this.game.add.tween(this.scale).to({y: 0}, Scrapyard.UIConstants.SCRAPYARD_FLIP_TIME / 2, Phaser.Easing.Sinusoidal.In, true);
	var bottomTween = this.game.add.tween(this.scale).to({y: 1}, Scrapyard.UIConstants.SCRAPYARD_FLIP_TIME / 2, Phaser.Easing.Sinusoidal.Out);
	topTween.chain(bottomTween);
	
	topTween.onComplete.add(function() {
		
		// Switch to successor's digit
		this.digit = (this.digit + 1) % 10;
		
		// Switch to digit's bottom frame
		this.frame = this.digit + 10;
		this.anchor.y = 0;
		
		this.bringToTop();	
	}, this);
	
	bottomTween.onComplete.add(function() {
		
		// This plates now completely covers its ancestor plate and we can remove the ancestor
		if (this.ancestor) {
			this.ancestor.remove();
		}
	}, this);
}

Scrapyard.UIPlateImage.prototype.remove = function() {
	
	this.kill();
}

Scrapyard.UIBootState = {
    create: function() {
		
        // Generally, we do not want to prevent default actions such as touch scrolling
        this.input.touch.preventDefault = false;

        // Do not pause when losing focus.
        this.game.stage.disableVisibilityChange = true;

        // Set scale mode to plain resize
        this.scale.scaleMode = Phaser.ScaleManager.RESIZE;
        
        this.state.start('Preload');
    }
};

Scrapyard.UIPreloadState = {
    preload: function() {
		           
        // Load game assets 
        this.load.spritesheet('plates', 'images/scrapyardPlates.png', 11, 21, 20);
    },

    create: function() {
		
        this.state.start('Main');
		
    }
};

Scrapyard.UIMainState = {
	scraps: null,
	scrapsAtUpdate: null,
	velocity: null,
	plates: [],
    
	updateTime: 0,
	updateScraps: 0,
	
	initialised: false,

    create: function() {
		
       	// Create plates group
		this.platesGroup = this.game.add.group();
		
        this.platesGroup.x = 4;
        
	  	// Get scraps and velocity
		this._getScraps(true);	
        
        this.scale.onSizeChange.add(this._onSizeChangeHandler, this);
        
    },

    _onSizeChangeHandler: function() {
        var unscaledPlatesWidth = this.platesGroup.getLocalBounds().width;
        
        var plateScale = (this.game.width - 8) / unscaledPlatesWidth;
        
        this.platesGroup.scale.setTo(plateScale);
    },
    	
    update: function() {
		
		if (this.initialised) {
		
			// Estimate and display scraps - delay for realism!
			if (Math.random() > 0.8) {
				this.scraps = this.scrapsAtUpdate + (this.game.time.now - this.updateTime) * this.velocity;
			}
			
			// Update digits
			// FIXME Make more robust to handle scraps with different number of digits
			var scraps = Math.floor(this.scraps).toString();
			for (var i = 0; i < scraps.length; i++) {
			
				// Check if plates matches desired scraps
				var digit = parseInt(scraps.charAt(i));
				if (this.plates[i].digit != digit) {
					
					// Check if the plate is old enough to flip
					if (this.game.time.now > this.plates[i].created + Scrapyard.UIConstants.SCRAPYARD_FLIP_DELAY) {
						
						// Spawn a new plate
						var plate = this._getAvailablePlate();
						var newDigit = (this.plates[i].digit + 1) % 10
						plate.spawn((Scrapyard.UIConstants.SCRAPYARD_PLATE_WIDTH + Scrapyard.UIConstants.SCRAPYARD_PLATE_SPACING) * i, Scrapyard.UIConstants.SCRAPYARD_PLATE_HEIGHT / 2, newDigit, false, this.plates[i]);
				
						// Flip old plate
						this.plates[i].flip();
						
						// Store references to new plate
						this.plates[i] = plate;
					}
				}
			}
		}
    },
	
	_getAvailablePlate: function() {
		
		// Get available plate from plates pool
		var plate = this.platesGroup.getFirstExists(false);
		
		// If there was no available plate we create a new one
		if (!plate) {
			plate = this.platesGroup.add(new Scrapyard.UIPlateImage(this.game));
		}
		
		return plate;
	},
	
	_getScraps: function(includeVelocity) {
        x_getScraps(includeVelocity, Scrapyard.UIMainState._getScraps_cb);
	},
    
    _getScraps_cb: function(r) {
        var result = JSON.parse(r)

		// Initialise
		if (!Scrapyard.UIMainState.initialised) {	
			Scrapyard.UIMainState.scraps = result.scraps;
			Scrapyard.UIMainState._init();
		}
		
		// Set or calculate velocity
		if (result.velocity != undefined) {	
			Scrapyard.UIMainState.velocity = result.velocity / 1000;
		} else {
			var deltaScraps = result.scraps - Scrapyard.UIMainState.updateScraps;							// Scraps since last update
			var discrepancy = result.scraps - Scrapyard.UIMainState.scraps;									// Difference between we are displaying and the actual scraps
			var deltaTime = Scrapyard.UIMainState.game.time.now - Scrapyard.UIMainState.updateTime;							// Ms since last update
			Scrapyard.UIMainState.velocity = Math.max(0, (deltaScraps + discrepancy * 0.25) / deltaTime);	// Scraps per ms
		}
		
		// Remember this update
		Scrapyard.UIMainState.updateScraps = result.scraps;
		Scrapyard.UIMainState.updateTime = Scrapyard.UIMainState.game.time.now;
		Scrapyard.UIMainState.scrapsAtUpdate = Scrapyard.UIMainState.scraps;
    },
	
	_init: function() {	
			
		// Initialise plates 
		var scraps = this.scraps.toString();
		for (var i = 0; i < scraps.length; i++) {
		
			var digit = parseInt(scraps.charAt(i));
		
			// Add bottom plate
			var bottomPlate = this._getAvailablePlate();
			bottomPlate.spawn((Scrapyard.UIConstants.SCRAPYARD_PLATE_WIDTH + Scrapyard.UIConstants.SCRAPYARD_PLATE_SPACING) * i, Scrapyard.UIConstants.SCRAPYARD_PLATE_HEIGHT / 2, digit, true);
			
			// Add top plate
			var topPlate = this._getAvailablePlate();
			topPlate.spawn((Scrapyard.UIConstants.SCRAPYARD_PLATE_WIDTH + Scrapyard.UIConstants.SCRAPYARD_PLATE_SPACING) * i, Scrapyard.UIConstants.SCRAPYARD_PLATE_HEIGHT / 2, digit, false, bottomPlate);			
			this.plates[i] = topPlate;
		}
		
		// Set up first update timer
		this.game.time.events.add(Scrapyard.UIConstants.SCRAPYARD_FIRST_UPDATE, function() {
			
			this._getScraps(false);
			
			// Set up following updates timer
			this.game.time.events.loop(Scrapyard.UIConstants.SCRAPYARD_FOLLOWING_UPDATES, function() {
				this._getScraps(false);
			}, this);
		}, this);
		
        this._onSizeChangeHandler();

		this.initialised = true;
	}	
};

