""" Use of YouTube API to get top videos of user TEDxTalks 
  Copyright amitch@rajgad.com, 2011
  
"""

import sys;
import gdata.youtube;
import gdata.youtube.service;

class YouTubeTEDxTalks :
    
  def __init__(self):
    self.service = gdata.youtube.service.YouTubeService()
    self.service.developer_key = 'AI39si5ejCxvKQyC3XZp1-6VRieVOTl16DwIX9IWYwTH_2Y5BnIEfSom5Oau0F2190nq9yf1QNDraZCnpndlvsminT5nCUxNxQ'
    self.service.client_id = 'TEDxTalks1'

  def gettopvideosbyquery(self):
    """Get top videos from user TEDxTalks"""
    query = gdata.youtube.service.YouTubeVideoQuery()
    
    query.max_results =10       #Max is 50
    query.start_index = 1
    query.racy = 'include'
    query.format='5'    # Web \ default format
    query.orderby = 'viewCount'
    query.author = 'TEDxTalks'
    
    videos = self.service.YouTubeQuery(query)

    for video in videos.entry:
        print video.media.title;

  def printtopvideosbyuser(self, count=100):
    """Get top viewed videos from user TEDxTalks"""
    
    username = 'TEDxTalks'
    orderby = 'viewCount'
    max_results = 50
    start_index = 1
    format='5'
    
    # Loop through count, max_results at a time
    while count > 0:
        if max_results > count:
            max_results = count
            
        count -= max_results
        
        uri = 'http://gdata.youtube.com/feeds/api/users/%s/uploads?max-results=%d&start-index=%d&orderby=%s&format=%s' \
         % (username, max_results, start_index, orderby,format)
        
        videos = self.service.GetYouTubeVideoFeed(uri)
    
        for video in videos.entry:
            PrintVideoSummary(video)

        start_index += max_results
         
class VideoSummary:
    def __init__(self, title, viewcount):
        this.title = title
        this.viewcount = viewcount
        
def PrintVideoSummary(video):
  print '%s,%s,%s' % (video.media.title.text, video.statistics.view_count, video.media.player.url)

def PrintVideoDetails(video):
  print 'Video title: %s' % video.media.title.text
  print 'Video published on: %s ' % video.published.text
  print 'Video description: %s' % video.media.description.text
  print 'Video category: %s' % video.media.category[0].text
  print 'Video tags: %s' % video.media.keywords.text
  print 'Video watch page: %s' % video.media.player.url
  print 'Video flash player URL: %s' % video.GetSwfUrl()
  print 'Video duration: %s' % video.media.duration.seconds

  # non video.media attributes
  print 'Video geo location: %s' % video.geo.location()
  print 'Video view count: %s' % video.statistics.view_count
  print 'Video rating: %s' % video.rating.average

  # show alternate formats
  for alternate_format in video.media.content:
    if 'isDefault' not in alternate_format.extension_attributes:
      print 'Alternate format: %s | url: %s ' % (alternate_format.type,
                                                 alternate_format.url)

  # show thumbnails
  for thumbnail in video.media.thumbnail:
    print 'Thumbnail url: %s' % thumbnail.url
    
# -----------------------------------------------------------------------------------------------
# The main entry point
def main():
  count = 200
  if len(sys.argv) > 1:
    count = sys.argv[1]
  
#  YouTubeTEDxTalks().gettopvideosbyquery()
  YouTubeTEDxTalks().printtopvideosbyuser(int(count))
  
if __name__ == "__main__":
    main()
