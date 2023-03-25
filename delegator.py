class Delegator:

    def __init__(self):
        self.delegations = {}

    def default(self, func):
        if self.delegations.get('default'):
            raise Exception("default already exists")
        self.delegations['default'] = func
        return func

    def delegate(self, case_name):
        def wrapper(func):
            if self.delegations.get(case_name):
                raise Exception("case_name already exists")
            self.delegations[case_name] = func
            return func
        return wrapper
    
    def switch(self, case_name, *args, **kwargs):
        func = self.delegations.get(case_name, self.delegations['default'])
        if not func:
            print("default option not found")
            return None
        return func(*args, **kwargs)
            
    
  
    







 
    
   