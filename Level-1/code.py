'''
////////////////////////////////////////////////////////////
///                                                      ///
///   0. tests.py is passing but the code is vulnerable  /// 
///   1. Review the code. Can you spot the bug?          ///
///   2. Fix the code but ensure that tests.py passes    ///
///   3. Run hack.py and if passing then CONGRATS!       ///
///   4. If stuck then read the hint                     ///
///   5. Compare your solution with solution.py          ///
///                                                      ///
////////////////////////////////////////////////////////////
'''

from collections import namedtuple
from decimal import *
# from decimal import Decimal
# from fractions import Fraction

Order = namedtuple('Order', 'id, items')
Item = namedtuple('Item', 'type, description, amount, quantity')

getcontext().prec = 1000
getcontext().traps[FloatOperation] = True
# getcontext().Emax = int(1e19)
# getcontext().Emin = int(-1e19)

def validorder(order: Order):
    # net = 0
    net = Decimal(0)
    for item in order.items:
        if item.type == 'payment':
            # net += item.amount * item.quantity
            net += (Decimal.from_float(item.amount) * Decimal.from_float(item.quantity))
            # net += (Decimal(item.amount) * Decimal(item.quantity))
        elif item.type == 'product':
            # net -= item.amount * item.quantity
            net -= (Decimal.from_float(item.amount) * Decimal.from_float(item.quantity))
            # net -= (Decimal(item.amount) * Decimal(item.quantity))
        else:
            return("Invalid item type: %s" % item.type)
    # print(net)
    # if net > Decimal(1e-5):
    if abs(net) > Decimal.from_float(1e-5):
        return("Order ID: %s - Payment imbalance: $%0.2f" % (order.id, net))
    else:
        return("Order ID: %s - Full payment received!" % order.id)
