# Class to test, parse_tedxvid.py, parse TEDx Videos from youtube
# Copyright, amitch@rajgad.com, 2011

import unittest;
from parse_tedxvid import *;

class TestParseTedXVid(unittest.TestCase):
    
    def setUp(self):
        self.video_list1 = [
                   "TEDxSeoul - Dr. Kim and Jung - 11/28/09,16947,https://www.youtube.com/watch?v=un4qbATrmx8&feature=youtube_gdata_player",
                   "TEDxCMU - Chris Guillebeau - Fear and Permission,16867,https://www.youtube.com/watch?v=unxL5RRhNb0&feature=youtube_gdata_player",
                   "TEDxCMU - Daniel Simons - Seeing The World As It Isn't,16781,https://www.youtube.com/watch?v=9Il_D3Xt9W0&feature=youtube_gdata_player",
                   "TEDxTokyo - Renee Byer - 5/22/09,16758,https://www.youtube.com/watch?v=Z3CDOS4GNdQ&feature=youtube_gdata_player",
                   "TEDxSF- Callie Curry aka Swoon,16622,https://www.youtube.com/watch?v=5298KZuW_JE&feature=youtube_gdata_player",
                   "TEDxVancouver - Nazanin Afshin-Jam - Voice for the Voiceless,16545,https://www.youtube.com/watch?v=soqtTCeczbM&feature=youtube_gdata_player",
                   "TEDxSF - Oana Pellea,16348,https://www.youtube.com/watch?v=OZdFErDoU3U&feature=youtube_gdata_player",
                   "TEDxVancouver - Jeet Kei Leung - Transformational Festivals,16335,https://www.youtube.com/watch?v=Q8tDpQp6m0A&feature=youtube_gdata_player",
                   "TEDxSF 2011 - Wade Adams - Nanotechnology and Energy,16270,https://www.youtube.com/watch?v=1GFst2IQBEM&feature=youtube_gdata_player",
                   "TEDxSF - Grow a New Eye,16153,https://www.youtube.com/watch?v=T-ldzLSFxds&feature=youtube_gdata_player"
                   ]
        
    # Test for single top conference          
    def test_parsevid1(self):
        parsevid = ParseTEDxVideos()
        topconf = parsevid.gettopconf(1, self.video_list1)

        self.assertEqual(topconf[0].split(",")[0], "TEDxSF")

    # Test for multiple top conference          
    def test_parsevid_top3(self):
        parsevid = ParseTEDxVideos()
        topconf_details = parsevid.gettopconf(3, self.video_list1)
        topconf =[]
        
        for topconf_detail in topconf_details:
         topconf.append(topconf_detail.split(",")[0])
         
        # If using Py 2.7
        #self.assertIn("TEDxSF", topconf)
        
        self.assertTrue("TEDxSF" in topconf)
        self.assertTrue("TEDxVancouver" in topconf)
        self.assertTrue("TEDxCMU" in topconf)
        self.assertFalse("TEDxTokyo" in topconf)
        
if __name__ == '__main__':
    unittest.main()        