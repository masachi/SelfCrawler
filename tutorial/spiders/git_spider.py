import scrapy


class GitSprider(scrapy.spiders.Spider):
    name = "git"
    allow_domains = ["github.com"]
    i = 2
    total = []
    start_urls = ["https://github.com/search?&q=repos%3A%3E%3D10&type=Users"]
    print total
    with open('../file/user.txt', 'w') as f:
        for user in total:
            f.write('http://github.com' + user + '\n');
    f.close()

    def parse(self, response):
        head = "https://github.com/search"
        page = "?p="
        tail = "&q=repos%3A%3E%3D10&type=Users"
        next_page = head + page + str(self.i) + tail
        name = response.xpath('//div[@class="d-flex"]/a/@href').extract()
        self.total.append(name)
        yield scrapy.Request(next_page, callback=self.parse, dont_filter=True)
        if self.i < 101:
            self.i = self.i + 1
            next_page = head + page + str(self.i) + tail
            yield scrapy.Request(next_page, callback=self.parse, dont_filter=True)
