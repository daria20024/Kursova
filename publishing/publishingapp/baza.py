
from .models import *

def get_contract():
    contracts = contract.objects.all()
    return contracts
