# Mystery Word

## Description

This is Mystery Word, in which you try to guess a randomly chosen word one
letter at a time.

## Deliverables

* A Git repo called mystery-word containing at least:
  * a `README.md` file explaining how to run your project
  * a `requirements.txt` file with any third-party packages needed
  * a suite of tests for your project


## TODO

In addition to the requirements from **Normal Mode**:

1. Let the user choose a level of difficulty at the beginning of the program.
Easy mode only has words of 4-6 characters; normal mode only has words of 6-10
characters; hard mode only has words of 10+ characters.

2. Add a loop so that when a game ends, the user is asked if they want to play
again and the game begins again if they reply in the positive.

### Nightmare Mode

Use the [PyGame](http://pygame.org/news.html) or [Kivy](http://kivy.org/)
libraries to make this a graphical experience.

## Notes

### Installing PyGame

PyGame is not a normal library. If you really want to try it, run the
following:

```sh
brew install sdl sdl_image sdl_mixer sdl_ttf portmidi
pip install hg+http://bitbucket.org/pygame/pygame
```

## Additional Resources

* [pytest](http://pytest.org/latest/).
* [Working with Text Files](https://opentechschool.github.io/python-data-intro/core/text-files.html)

## Credit

This lab is based off a similar exercise in MIT's 6.00.1x course.
