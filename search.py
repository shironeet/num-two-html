import sys

from geocoder import get_ll_span
from mapapi import show_map


def main():
    toponym_to_find = " ".join(sys.argv[1:])

    if toponym_to_find:
        ll, spn = get_ll_span(toponym_to_find)
        ll_spn = f"ll={ll}&spn={spn}"

        point_param = f"pt={ll}"
        show_map(ll_spn, "map", add_params=point_param)
    else:
        print('No data')


if __name__ == "__main__":
    main()
