from datetime import date, timedelta

from django.core.management.base import BaseCommand
from django.db import transaction

from user.models import Author, Blog, Entry


BLOGS = [
    ("Beatles Blog", "All the latest Beatles news."),
    ("Cheddar Talk", "Thoughts on cheese."),
    ("Django Weblog", "News about Django."),
    ("Quiet Corner", "No posts yet — useful for empty reverse FK lookups."),
    ("Python Daily", "Short notes on Python."),
    ("SQL Kitchen", "Queries, indexes, and plans."),
    ("Travel Logs", "Places, trains, and delayed flights."),
    ("Coffee Notes", "Beans, brew, and cafes."),
    ("Indie Games", "Small games, big ideas."),
    ("Photo Walks", "Streets, light, and film."),
    ("Kitchen Experiments", "Recipes that almost worked."),
    ("Open Source Diary", "PRs, issues, and maintainers."),
    ("Classic Cinema", "Old films, new takes."),
    ("Garden Patch", "Tomatoes, weeds, and rain."),
    ("Running Club", "Miles, splits, and blisters."),
    ("Space Watch", "Rockets, planets, and night sky."),
    ("Folk Tunes", "Songs, strings, and stories."),
    ("City Bikes", "Lanes, locks, and hills."),
    ("Board Game Night", "Dice, cards, and table talk."),
    ("Language Lab", "Words, grammar, and mistakes."),
]

AUTHORS = [
    ("John Lennon", "john@beatles.com"),
    ("Paul McCartney", "paul@beatles.com"),
    ("George Harrison", "george@beatles.com"),
    ("Ringo Starr", "ringo@beatles.com"),
    ("Lennon", "lennon@solo.com"),
    ("Nobody Posted", "nobody@example.com"),
    ("Ada Lovelace", "ada@math.org"),
    ("Alan Turing", "alan@bletchley.uk"),
    ("Grace Hopper", "grace@navy.mil"),
    ("Linus Torvalds", "linus@kernel.org"),
    ("Guido van Rossum", "guido@python.org"),
    ("Margaret Hamilton", "margaret@apollo.nasa"),
    ("Katherine Johnson", "katherine@nasa.gov"),
    ("Dennis Ritchie", "dmr@bell-labs.com"),
    ("Barbara Liskov", "liskov@mit.edu"),
    ("Donald Knuth", "knuth@stanford.edu"),
    ("Radia Perlman", "radia@network.org"),
    ("Tim Berners-Lee", "timbl@w3.org"),
    ("Jean Bartik", "jean@eniac.org"),
    ("Hedy Lamarr", "hedy@frequency.com"),
]


def _entries(blogs, authors):
    """25 entries so user_entry has 20+ rows and M2M links stay varied."""
    b, a = blogs, authors
    today = date.today()
    return [
        {
            "blog": b[0],
            "headline": "New Lennon Biography",
            "body_text": "A new book about John Lennon.",
            "pub_date": date(2008, 3, 3),
            "mod_date": date(2008, 3, 4),
            "number_of_comments": 10,
            "number_of_pingbacks": 2,
            "rating": 5,
            "authors": [a[0], a[1]],
        },
        {
            "blog": b[0],
            "headline": "The Lennon Legend",
            "body_text": "Remembering Lennon.",
            "pub_date": date(2007, 6, 1),
            "mod_date": date(2007, 6, 1),
            "number_of_comments": 4,
            "number_of_pingbacks": 4,
            "rating": 4,
            "authors": [a[0]],
        },
        {
            "blog": b[0],
            "headline": "Beatles reunion rumours",
            "body_text": "Just rumours.",
            "pub_date": date(2005, 12, 31),
            "mod_date": date(2006, 1, 2),
            "number_of_comments": 0,
            "number_of_pingbacks": 8,
            "rating": 2,
            "authors": [a[1], a[2], a[3]],
        },
        {
            "blog": b[0],
            "headline": "Paul on tour",
            "body_text": "World tour announced.",
            "pub_date": date(2020, 1, 15),
            "mod_date": date(2020, 2, 1),
            "number_of_comments": 25,
            "number_of_pingbacks": 1,
            "rating": 5,
            "authors": [a[1]],
        },
        {
            "blog": b[0],
            "headline": "new lennon biography",
            "body_text": "Same words, different case — useful for iexact.",
            "pub_date": date(2008, 3, 3),
            "mod_date": date(2008, 3, 5),
            "number_of_comments": 1,
            "number_of_pingbacks": 0,
            "rating": 3,
            "authors": [a[4]],
        },
        {
            "blog": b[1],
            "headline": "Best cheddar in Wisconsin",
            "body_text": "Cheese ranking.",
            "pub_date": date(2006, 5, 20),
            "mod_date": date(2006, 5, 21),
            "number_of_comments": 7,
            "number_of_pingbacks": 0,
            "rating": 5,
            "authors": [a[2]],
        },
        {
            "blog": b[1],
            "headline": "Why brie is overrated",
            "body_text": "Opinion piece with no authors.",
            "pub_date": date(2006, 11, 11),
            "mod_date": date(2006, 11, 11),
            "number_of_comments": 12,
            "number_of_pingbacks": 12,
            "rating": 1,
            "authors": [],
        },
        {
            "blog": b[2],
            "headline": "Django 4.2 released",
            "body_text": "LTS release notes.",
            "pub_date": date(2023, 4, 3),
            "mod_date": date(2023, 4, 10),
            "number_of_comments": 40,
            "number_of_pingbacks": 9,
            "rating": 5,
            "authors": [a[0], a[1], a[2], a[3]],
        },
        {
            "blog": b[2],
            "headline": "QuerySets are lazy",
            "body_text": "They hit the DB only when evaluated.",
            "pub_date": date(2023, 4, 20),
            "mod_date": date(2023, 4, 21),
            "number_of_comments": 3,
            "number_of_pingbacks": 20,
            "rating": 4,
            "authors": [a[1], a[10]],
        },
        {
            "blog": b[2],
            "headline": "ORM cheat sheet",
            "body_text": "filter, exclude, annotate.",
            "pub_date": date(2024, 1, 1),
            "mod_date": today,
            "number_of_comments": 0,
            "number_of_pingbacks": 0,
            "rating": 5,
            "authors": [a[3]],
        },
        {
            "blog": b[0],
            "headline": "Ringo drum clinic",
            "body_text": "Live event.",
            "pub_date": date(2019, 8, 8),
            "mod_date": date(2019, 8, 9),
            "number_of_comments": 6,
            "number_of_pingbacks": 6,
            "rating": 4,
            "authors": [a[3], a[1]],
        },
        {
            "blog": b[1],
            "headline": "Lennon likes cheese",
            "body_text": "Crossover post for related lookups.",
            "pub_date": date(2008, 7, 7),
            "mod_date": date(2008, 7, 8),
            "number_of_comments": 2,
            "number_of_pingbacks": 1,
            "rating": 3,
            "authors": [a[0], a[4]],
        },
        {
            "blog": b[4],
            "headline": "Walrus operator in the wild",
            "body_text": "Assignment expressions in Python 3.8+.",
            "pub_date": date(2021, 2, 14),
            "mod_date": date(2021, 2, 15),
            "number_of_comments": 9,
            "number_of_pingbacks": 3,
            "rating": 4,
            "authors": [a[10], a[6]],
        },
        {
            "blog": b[5],
            "headline": "EXPLAIN ANALYZE without fear",
            "body_text": "Reading query plans.",
            "pub_date": date(2022, 9, 1),
            "mod_date": date(2022, 9, 3),
            "number_of_comments": 18,
            "number_of_pingbacks": 18,
            "rating": 5,
            "authors": [a[9], a[13]],
        },
        {
            "blog": b[6],
            "headline": "Night train to Lisbon",
            "body_text": "A delayed sleeper and a good book.",
            "pub_date": date(2018, 11, 20),
            "mod_date": date(2018, 11, 22),
            "number_of_comments": 5,
            "number_of_pingbacks": 0,
            "rating": 4,
            "authors": [a[18], a[19]],
        },
        {
            "blog": b[7],
            "headline": "Pour-over vs espresso",
            "body_text": "Taste notes from two cafes.",
            "pub_date": date(2022, 3, 12),
            "mod_date": date(2022, 3, 12),
            "number_of_comments": 14,
            "number_of_pingbacks": 2,
            "rating": 3,
            "authors": [a[7]],
        },
        {
            "blog": b[8],
            "headline": "A puzzle game in 48 hours",
            "body_text": "Game jam recap.",
            "pub_date": date(2021, 10, 31),
            "mod_date": date(2021, 11, 2),
            "number_of_comments": 22,
            "number_of_pingbacks": 5,
            "rating": 5,
            "authors": [a[9], a[14], a[15]],
        },
        {
            "blog": b[9],
            "headline": "Golden hour on film",
            "body_text": "Portra 400 and a borrowed camera.",
            "pub_date": date(2017, 6, 21),
            "mod_date": date(2017, 6, 22),
            "number_of_comments": 8,
            "number_of_pingbacks": 8,
            "rating": 4,
            "authors": [a[19]],
        },
        {
            "blog": b[10],
            "headline": "Sourdough that refused to rise",
            "body_text": "Notes from a failed bake.",
            "pub_date": date(2020, 4, 4),
            "mod_date": date(2020, 4, 5),
            "number_of_comments": 11,
            "number_of_pingbacks": 1,
            "rating": 2,
            "authors": [a[8], a[18]],
        },
        {
            "blog": b[11],
            "headline": "First good bug report",
            "body_text": "Repro steps, logs, and a patch.",
            "pub_date": date(2019, 1, 9),
            "mod_date": date(2019, 1, 10),
            "number_of_comments": 16,
            "number_of_pingbacks": 7,
            "rating": 5,
            "authors": [a[9], a[10], a[14]],
        },
        {
            "blog": b[12],
            "headline": "Watching Casablanca again",
            "body_text": "Dialogue that still lands.",
            "pub_date": date(2016, 12, 25),
            "mod_date": date(2016, 12, 26),
            "number_of_comments": 3,
            "number_of_pingbacks": 9,
            "rating": 5,
            "authors": [a[16]],
        },
        {
            "blog": b[14],
            "headline": "Ten kilometres in the rain",
            "body_text": "A wet Sunday loop.",
            "pub_date": date(2024, 2, 11),
            "mod_date": date(2024, 2, 12),
            "number_of_comments": 0,
            "number_of_pingbacks": 0,
            "rating": 3,
            "authors": [a[12], a[11]],
        },
        {
            "blog": b[15],
            "headline": "A clear night for Jupiter",
            "body_text": "Binoculars on the balcony.",
            "pub_date": date(2023, 8, 15),
            "mod_date": date(2023, 8, 16),
            "number_of_comments": 13,
            "number_of_pingbacks": 4,
            "rating": 4,
            "authors": [a[11], a[12], a[17]],
        },
        {
            "blog": b[17],
            "headline": "Climbing the last hill home",
            "body_text": "Gears, wind, and a flat tire.",
            "pub_date": today - timedelta(days=40),
            "mod_date": today - timedelta(days=39),
            "number_of_comments": 6,
            "number_of_pingbacks": 2,
            "rating": 3,
            "authors": [a[17], a[7]],
        },
        {
            "blog": b[18],
            "headline": "Teaching Catan to newcomers",
            "body_text": "Sheep, wheat, and table talk.",
            "pub_date": today - timedelta(days=7),
            "mod_date": today,
            "number_of_comments": 21,
            "number_of_pingbacks": 21,
            "rating": 5,
            "authors": [a[15], a[16], a[8]],
        },
    ]


class Command(BaseCommand):
    help = (
        "Insert sample Blog, Author, and Entry rows (20+ each), including "
        "many-to-many links in user_entry_authors."
    )

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete existing Blog/Author/Entry rows before inserting.",
        )

    @transaction.atomic
    def handle(self, *args, **options):
        if options["clear"]:
            Entry.objects.all().delete()
            Author.objects.all().delete()
            Blog.objects.all().delete()
            self.stdout.write(self.style.WARNING("Cleared existing blog data."))

        blogs = Blog.objects.bulk_create(
            [Blog(name=name, tagline=tagline) for name, tagline in BLOGS]
        )
        authors = Author.objects.bulk_create(
            [Author(name=name, email=email) for name, email in AUTHORS]
        )

        through_count = 0
        for item in _entries(blogs, authors):
            author_list = item.pop("authors")
            entry = Entry.objects.create(**item)
            if author_list:
                entry.authors.set(author_list)
                through_count += len(author_list)

        self.stdout.write(
            self.style.SUCCESS(
                "Inserted "
                f"{len(blogs)} blogs, {len(authors)} authors, "
                f"{Entry.objects.count()} entries, "
                f"{through_count} entry-author links."
            )
        )
        self.stdout.write(
            "Quiet Corner has no entries; Nobody Posted has no entries; "
            "one cheddar post has no authors — useful for ORM empty lookups."
        )
