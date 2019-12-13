import re
from bowler.query import Query

def main():
    (
        Query()
        .select_var("x")
        .rename("p1")
        .select_var("y")
        .rename("p2")
        .select_var("z")
        .rename("p3")
        .select_var("r_b")
        .rename("relative_base")
        .select_var("pos")
        .rename("position")
        .idiff()
    )

