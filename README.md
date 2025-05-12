# Setup
- Two DC motors host two spool of line which go through pulleys and swings the boom and the jib respectively.
- One servo motor (somehow - TBD) is attached to a tiller.

## Testing Setup
- The lines raise/lower two washers, respectively.
- The servo just rotates min/max.

## Running
With the full setup
```
import actuators1 as a
a.down() # moves washer1 down
a.up() # moves washer1 up
a.up2() # moves washer2 up
a.down2() # moves washer2 down
a.right() # servo
a.left()
```
