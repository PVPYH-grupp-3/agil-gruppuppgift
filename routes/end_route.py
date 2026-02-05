from flask import Blueprint, render_template

end_bp = Blueprint("end", __name__, url_prefix="/end")

@end_bp.route("/")
def end():
    return render_template("end.html")
    