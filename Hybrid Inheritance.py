class CreativeEntrepreneur:
    def __init__(self, trending_topic):
        self.trending_topic = trending_topic  


class RawDesigner(CreativeEntrepreneur):
    def designContent(self):
        print("Creating bold and attention-grabbing visuals for the content.")


class ContentStrategist(CreativeEntrepreneur):
    def planStrategy(self):
        print("Developing the content strategy and identifying the target audience.")



class TalesFromTheIslandsCreator(RawDesigner, ContentStrategist):
    def produceReel(self):
        print("Creating a video reel centered around the trending topic.")
        if self.trending_topic.lower() == "conspiracy theories":
            print("The content will revolve around conspiracy theories.")
        elif self.trending_topic.lower() == "motivational stories":
            print("The content will focus on motivational stories.")
        else:
            print("The content will focus on a general topic.")


creator = TalesFromTheIslandsCreator("Conspiracy Theories")
creator.designContent()  
creator.planStrategy()  
creator.produceReel() 


creator2 = TalesFromTheIslandsCreator("Motivational Stories")
creator2.designContent()
creator2.planStrategy()
creator2.produceReel()
