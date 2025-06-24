# Asteroids PyGame

Destroy the asteroids by shooting from your spaceship!

## Prerequisites

- Python 3.11

## Setup

1. Create a python virtual environment and activate it:

    ```bash
    $ virtualenv -p `which python3.11` .venv
    $ source .venv/bin/activate
    (.venv) $ which pip
    /path/to/your/venv/bin/pip
    ```

2. Install dependencies:

    ```bash
    (.venv) $ pip install -r requirements.txt
    ```

3. Run and enjoy:

    ```bash
    (.venv) $ python main.py
    ```

## Next steps

- [ ] Add a scoring system
- [ ] Implement multiple lives and respawning
- [ ] Add an explosion effect for the asteroids
- [ ] Add acceleration to the player movement
- [ ] Make the objects wrap around the screen instead of disappearing
- [ ] Add a background image
- [ ] Create different weapon types
- [ ] Make the asteroids lumpy instead of perfectly round
- [ ] Make the ship have a triangular hit box instead of a circular one
- [ ] Add a shield power-up
- [ ] Add a speed power-up
- [ ] Add bombs that can be dropped
