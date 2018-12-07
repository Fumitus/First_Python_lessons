
import logging
logging.basicConfig(filename = 'myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.DEBUG)

logging.debug('Start of Program')

def factorial(n):
    logging.debug('Start of factorial(%s)' % (n))
    total = 1
    for i in range(1, n + 1):
        total *= i
        logging.info('i is %s, total is %s' % (i, total))

    logging.debug('Return value is %s' % (total))  
    return total

print(factorial(6))


logging.debug('End of Program')
