class ContentCreator:
    def __init__(self, name, followers):
        self.name = name
        self.followers = followers

    def createPost(self):
        if self.followers < 1000:
            print(f"{self.name} is creating a video. Lets go followers!")
        else:
            print(f"{self.name} is keep grinding!. You are popular now!")


class Tiktoker(ContentCreator):
    def __init__(self, name, followers):
       
        super().__init__(name, followers)

    def recordVideo(self):
        print(f"{self.name} is recording a new TikTok video!")


creator = ContentCreator("Malacash", 500)
creator.createPost() 

tiktoker = Tiktoker("SnoopCat", 1500)
tiktoker.createPost()  
tiktoker.recordVideo()  