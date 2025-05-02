from alltypes.data.hashtable import HashTable
from alltypes.data.term import Term
from prims.cp._identifiers import CP_Ident

class CP_Variable:
    
    @staticmethod
    def create(args):
        from prims.cp._system import CP_System
        system = args[0]
        var_name = args[1]
        domain = args[2]
        variable = Term.create('CP_Variable', name=var_name, domain=domain)
        attrib = HashTable.create(domain=domain, system=system)
        variable.set_attrib(attrib)
        CP_System.add_variable(system, variable)
        return variable
    
    @staticmethod
    def name(variable):
        return variable[CP_Ident.NAME]
    
    @staticmethod
    def domain(variable):
        return variable.get_attrib()[CP_Ident.DOMAIN]

    @staticmethod
    def set_domain(variable, domain):
        variable.get_attrib()[CP_Ident.DOMAIN] = domain