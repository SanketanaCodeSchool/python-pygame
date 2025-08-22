# Game Assets

This folder is for storing game assets like images, sounds, and other resources.

## Current Assets
The current version of the cookie clicker game creates assets programmatically (drawing the cookie with circles), but you can enhance it by adding:

## Suggested Assets to Add

### Images
- `cookie.png` - A better looking cookie image
- `button_normal.png` - Normal button background
- `button_hover.png` - Button background when hovered
- `background.png` - Game background image

### Sounds
- `click.wav` - Sound when clicking the cookie
- `buy.wav` - Sound when purchasing upgrades
- `background_music.mp3` - Background music

## How to Add Assets

1. Place your image/sound files in this folder
2. Load them in the game using:
   ```python
   # For images
   cookie_image = pygame.image.load("assets/cookie.png")
   
   # For sounds
   click_sound = pygame.mixer.Sound("assets/click.wav")
   ```

## Asset Requirements

### Images
- **Format**: PNG or JPG
- **Size**: Keep reasonable sizes (under 1MB each)
- **Style**: Simple, clean, and appropriate for middle school students

### Sounds
- **Format**: WAV or MP3
- **Duration**: Keep sound effects short (under 2 seconds)
- **Volume**: Not too loud, appropriate for classroom use

## Free Asset Resources
- **Images**: Pixabay, Unsplash, OpenGameArt.org
- **Sounds**: Freesound.org, OpenGameArt.org
- **Fonts**: Google Fonts, DaFont.com

Remember to check licensing and give credit when using external assets!
