import yankee
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor

def main():

    process = CrawlerRunner()

    # Default: a popular candle
    spider1 = yankee.YankeecandleSpider()
    process.crawl(spider1)

    # Current most popular
    spider2 = yankee.YankeecandleSpider(
        name = "yankeeCandle2",
        url="https://www.amazon.com/Yankee-Candle-Large-Midsummers-Night/product-reviews/B000ORX6WI/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews/"
    )
    process.crawl(spider2)

    # Run
    d = process.join()
    d.addBoth(lambda _: reactor.stop())

    reactor.run()

if __name__ == "__main__":
    main()

