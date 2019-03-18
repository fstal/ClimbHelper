class ClimbSite:
    """A class repr. climbing sites for our program.

    Attributes:
        name: A string representing the name of the climbing location.
        indoor: A bool representing whether there is indoor climbing.
        outdoor: A bool representing whether there is outdoor climbing.
        bouldering: A bool representing whether there is bouldering.
        top: A bool representing whether there is traditional climbing (rope-climbing).
        coords: A string representing the coordinates for the climbing site.
        diffs: A list of strings representing the different difficulties found at the climbing site.
        desc: A string representing a description of the climbing site.
    """
    siteCount = 0

    def __init__(self, name, indoor, outdoor, bouldering, top, coords, diffs, desc):
        self.name = name                # string
        self.indoor = indoor            # bool
        self.outdoor = outdoor          # bool
        self.bouldering = bouldering    # bool
        self.top = top                  # bool
        self.coords = coords            # string
        self.diffs = diffs              # list of strings
        self.desc = desc                # string
        ClimbSite.siteCount += 1

    def display_sitecount(self):
        """
        Prints the amount of ClimbSite objects
        """
        print('There are ' + str(ClimbSite.siteCount) + ' ClimbSite objects currently')

    def __str__(self):
        """
        Overrides method called with print(ClimbSite-object)
        """
        nam = 'Name: ' + self.name
        if self.indoor:
            ind = 'Indoor climbing: Yes'
        else:
            ind = 'Indoor climbing: No'
        if self.outdoor:
            out = 'Outdoor climbing: Yes'
        else:
            out = 'Outdoor climbing: No'
        if self.bouldering:
            bould = 'Bouldering: Yes'
        else:
            bould = 'Bouldering: No'
        if self.top:
            top_ = 'Top rope climbing: Yes'
        else:
            top_ = 'Top rope climbing: No'
        coord = 'Coordinates: ' + self.coords
        diffis = ""
        for i in self.diffs:
            diffis += str(i) + " "
        diff = 'Difficulties: ' + diffis
        des = 'Description: ' + self.desc
        return ' %s\n %s\n %s\n %s\n %s\n %s\n %s\n %s' % (nam, ind, out, bould, top_, coord, diff, des)
