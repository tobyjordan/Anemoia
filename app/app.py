import flask
from flask_moment import Moment

import aggregator


app = flask.Flask("__name__")

moment = Moment(app)

entries = aggregator.NewsAggregator().get_latest()
latest_feed = entries[:5]
curated_feed = entries[5:9]
more_feed = entries[10:15]

@app.route("/")
def index():
  return flask.render_template("index.html", latest_feed=latest_feed, curated_feed=curated_feed, more_feed=more_feed)

@app.route("/about")
def about():
  return flask.render_template("about.html")
