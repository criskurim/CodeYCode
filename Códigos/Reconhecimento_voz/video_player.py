import vlc 
Instance = vlc.Instance() 
player = Instance.media_player_new() 
Media = Instance.media_new('https://www.youtube.com/watch?v=T5uXIl9bbtY&t=412s') 
Media.add_option('network-caching=1') 
player.set_media(Media) 
player.play() 


