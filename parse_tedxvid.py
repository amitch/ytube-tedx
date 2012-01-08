# Class to parse TEDx Videos from youtube
# Copyright, amitch@rajgad.com, 2011

import sys;
from heapq import *;

class ParseTEDxVideos:
  vidfile = ''
  def __init__(self, vidfile=None):
      if vidfile is not None:
          self.vidfile = vidfile
          self.file = open(vidfile, "r")


  def gettopconf(self, count=10, conflist=None):
      conferences = {}
      topconf = []  

      if conflist is None:
          conflist = self.file
          
      # Each line is a conference, store in a directory, increasing counts subsequently
      for line in conflist:
        conference = line.split()[0]
        if conferences.has_key(conference):
          conference_item = conferences[conference]
          conference_item[0] += 1
          conferences[conference] = conference_item
        else:
          conferenceuri = line.split(',')[2]
          conferences[conference] = [1,conferenceuri]

      # Put these in heapq, using negative of video count to remove top ones
      h = []
      for conference in conferences.items():
        heappush(h, (-1 * conference[1][0], conference[0], conference[1][1]))

      # Remove count
      for i in range(count):
        views, conference, conferenceuri = heappop(h)
        topconf.append('%s,%d,%s' %(conference, -1*views, conferenceuri))
        #print '%s,%d,%s' %(conference, -1*views, conferenceuri)
        
      return topconf
      
# -----------------------------------------------------------------------------------------------
# The main entry point
def main():
  vidfile ='tedxtalks-vids-1k.txt'
  count = 11
  if len(sys.argv) > 1:
    vidfile = sys.argv[1]
    if len(sys.argv) > 2:
      count = sys.argv[2]
    
  parsevid = ParseTEDxVideos(vidfile)
  for conf in parsevid.gettopconf(int(count)):
      print conf
  
if __name__ == "__main__":
    main()
