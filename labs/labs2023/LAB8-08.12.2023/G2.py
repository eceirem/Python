class Book():
    def __init__(self,title,author, publisher, page_count ):
        self.t = title
        self.a = author
        self.p = publisher
        self.pc = page_count
class Periodical_Publication(Book):
    def __init__(self, title, author, publisher, page_count, period):
        super().__init__(title, author, publisher, page_count)
        self.per = period
    def get_period(self):
        return self.per
    
    def __str__(self):
        return "Periodical Publication: Title: {}, Author: {},Publisher: {} ,Page Count: {},Period: {}".format(self.t,self.a,self.p,self.pc,self.per)
    
class Audio_Publication(Book):
    def __init__(self, title, author, publisher, page_count,narrator):
        super().__init__(title, author, publisher, page_count)
        self.n = narrator

    def get_narrator(self):
        return self.n
    
    def __str__(self):
        return "Audio Publication: Title: {}, Author: {},Publisher: {} ,Page Count: {},Narrator: {}".format(self.t,self.a,self.p,self.pc,self.n)
    
class Academic_Publication(Book):
    papers = ["First","Second","Third"]
    new_papers = []
    def __init__(self, title, author, publisher, page_count,field):
        super().__init__(title, author, publisher, page_count)
        self.f = field
    def control_and_add_paper(self,paper):
        if paper in self.papers:
            return "{} already in the predefined_papers.".format(paper)
        else:
            self.new_papers.append(paper)
            return "{} added to the papers.".format(paper)
    def remove_paper(self,paper):
        if paper in self.new_papers:
            self.new_papers.remove(paper)
            return "{} removed from the papers.".format(paper)
        else:
            return "{} in not in the papers.".format(paper)
        
    def get_papers(self):
        return self.new_papers

    def get_field(self):
        return self.f
    
    def __str__(self):
        return "Academic Publication: Title: {}, Author: {},Publisher: {} ,Page Count: {}, Field: {} Papers: {}".format(self.t,self.a,self.p,self.pc,self.f, ",".join(self.new_papers))

academic1 = Academic_Publication("Academic Study","Academic Author","Science Publications",300,"Computer Science")
periodical1 = Periodical_Publication("Magazine Name","Name","Publisher",50,"Monthly")
audio1 = Audio_Publication("Audiobook Name","Narrtor Author", "Audiobook Publishers",200,"Narrator Person")
print(academic1.control_and_add_paper("Frst"))
print(academic1.control_and_add_paper("Scnd"))
print(academic1.control_and_add_paper("Third"))
print(academic1.remove_paper("Thir"))
print(academic1.remove_paper("Frst"))
print(academic1)
print(periodical1)
print(audio1)