class GraphicDesigner:
    def designLogo(self):
        print("Creative design for logo for visual brand .")


class WebDeveloper:
    def buildWebsite(self):
        print("Building a website for the brand's online presence.")


class DigitalSolutionsProvider(GraphicDesigner, WebDeveloper):
    def deliverProject(self):
        print("Delivering a complete project: ")
        self.designLogo()  
        self.buildWebsite() 


provider = DigitalSolutionsProvider()
provider.deliverProject()  