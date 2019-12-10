test_map = 'COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L'

orbit_list = []

direct_orbits = 0
indirect_orbits = 0

class orbit():
    def __init__(self, e, co = None):
        self.element_name = ""
        self.origin = False
        self.orbits = []
        self.orbited_by = []
        self.element_name = e
        if e == 'COM':
            self.origin = True
        self.orbits.append(co)
        
    def new_orbit(self, o, co):
        global indirect_orbits
        no = orbit(o, co)
        #self.orbited_by.append(no)
        orbit_list[0].orbited_by.append(no)
        return no

    def get_name(self):
        return self.element_name

if __name__ == "__main__":
    
    current_orbit = None
    first = True
    found_orbit = False
    for o in test_map:
        for n in o.split(')'):
            if first == True:
                for x in orbit_list:
                    if x.get_name() == n:
                        current_orbit = x
                        found_orbit = True
                if found_orbit == True:
                    first = False
                    continue
                else:
                    current_orbit = orbit(n)
                    first = False
            else:
                current_orbit = current_orbit.new_orbit(n, current_orbit)
            orbit_list.append(current_orbit)
        first = True

    direct_orbits = len(orbit_list)-1
    print('Total number of orbits: ', direct_orbits+len(orbit_list[0].orbited_by))
    pass