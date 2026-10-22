
import os

from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = os.environ.get(
    "SECRET_KEY",
    "change-this-before-deploying"
)


# PORTFOLIO PROJECTS
projects = [
    {
        "name": "Rose Studio",
        "category": "FASHION & LIFESTYLE E-COMMERCE",
        "description": (
            "A bold, editorial-style fashion and lifestyle store "
            "featuring product filters, an interactive shopping cart, "
            "and a checkout demo."
        ),
        "tech": "HTML · CSS · JavaScript",
        "image": "images/rose-studio.png",
        "link": "https://rose-fashion.netlify.app/",
        "link_label": "Live Demo"
    },
    {
        "name": "Glam by Anaya",
        "category": "BEAUTY & MAKEUP",
        "description": (
            "An elegant bridal makeup website showcasing beauty "
            "services, a visual gallery, and WhatsApp enquiry functionality."
        ),
        "tech": "HTML · CSS · JavaScript",
        "image": "images/glam-by-anaya.png",
        "link": "https://glam-by-anaya.netlify.app/",
        "link_label": "Live Demo"
    },
    {
        "name": "Rivals Gift Studio",
        "category": "GIFTING & HAMPERS",
        "description": (
            "A premium gifting storefront featuring curated hampers, "
            "product collections, a shopping cart, and WhatsApp enquiries."
        ),
        "tech": "HTML · CSS · JavaScript",
        "image": "images/rivals-gift-studio.png",
        "link": "https://rivals-gift-studio.netlify.app/",
        "link_label": "Live Demo"
    },
    {
        "name": "The Grand Escape Resort",
        "category": "HOSPITALITY & TRAVEL",
        "description": (
            "A luxurious, palace-inspired resort website featuring "
            "destination visuals, room enquiries, and a demo booking form."
        ),
        "tech": "HTML · CSS · JavaScript",
        "image": "images/grand-escape-resort.png",
        "link": "https://the-grand-escape-resort.netlify.app/",
        "link_label": "Live Demo"
    }
]


# HOME PAGE
@app.route("/")
def home():
    return render_template("index.html", projects=projects)


# OPTIONAL: keep this route for old links.
# The contact form itself must submit directly to FormSubmit.
@app.route("/contact", methods=["POST"])
def contact():
    from flask import redirect, url_for

    return redirect(url_for("home") + "#contact")


if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
