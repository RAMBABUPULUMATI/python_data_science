import  logging
import math
# create and configure logger
LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename = "C:\\Users\\Prashant_Palod\\PycharmProjects\\Python_test\\Log_out_put.log",
                    level = logging.DEBUG,
                    format = LOG_FORMAT,
                    filemode = 'w')
logger = logging.getLogger()

# Test the logger
logger.info("Our first message")
print(logger.level)

# Level, Numeric Value in logger
# NOTSET = 0 , DEBUG = 10, INFO = 20 , WARNING = 30, ERROR = 40, CRITICAL = 50
# The loggin level basically is set to 30 in basic logging , so you need to reset it again

def quadratic_formula(a, b, c):
    """Return the solutions to the equation ax^2 + bx + c = 0."""
    logger.info("quadratic_formula({0}, {1}, {2})".format(a, b, c))

    # Compute the discriminant
    logger.debug("compute the discriminant")
    disc = b**2 - 4*a*c

    # compute the two roots
    logger.debug("compute the two roots")
    root1 = (-b + math.sqrt(disc)) / (2*a)
    root2 = (-b - math.sqrt(disc)) / (2*a)

    # Return the roots
    logger.debug(" Return the roots")
    return (root1, root2)

roots = quadratic_formula(1,0,-4)


print(roots)