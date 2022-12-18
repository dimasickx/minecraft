from enderman_portal import find_portal, Point, Coordinates
import argparse as argp


def parse_args():
    parser = argp.ArgumentParser()
    parser.add_argument('-t1', '--first_throw', action='store', help="example: -t1 'x z angle'")
    parser.add_argument('-t2', '--second_throw', action='store', help="example: -t2 'x z angle'")
    args = parser.parse_args()
    x1, y1, alpha1 = map(float, args.first_throw.split())
    x2, y2, alpha2 = map(float, args.second_throw.split())
    return x1, y1, alpha1, x2, y2, alpha2


def main():
    x1, y1, alpha1, x2, y2, alpha2 = parse_args()
    result: Point = find_portal(Coordinates(x1, y1, alpha1), Coordinates(x2, y2, alpha2))
    print(f'x: {result.x} z: {result.y}')


if __name__ == '__main__':
    main()
