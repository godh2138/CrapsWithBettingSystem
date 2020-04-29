
import time
import sys
import main as craps

build_version = '4.2.1'
current_time = time.asctime(time.localtime(time.time()))
print("\n\nBuild Version:", build_version,
      "\nTime:", str(current_time), "\n\n")
# -------------------------------------------------------------------------

try:
    game = craps.Game()
    game.start()
except KeyboardInterrupt:
    print('\nGamed ended by user!')
    # TODO: Maybe a little game summary here
    # This is a good idea, perhaps roll and win/loss history!
