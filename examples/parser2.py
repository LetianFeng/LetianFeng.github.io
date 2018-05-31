#!/usr/bin/python3

import argparse


def main(args):
    answer = args.x**args.y
    if args.bias:
        answer += args.bias

    if args.quiet:
        print(answer)
    elif args.verbose:
        if args.bias:
            print("{} to the power {} plus bias {} equals {}".format(args.x, args.y, args.bias, answer))
        else:
            print("{} to the power {} equals {}".format(args.x, args.y, answer))
    else:
        if args.bias:
            print("{}^{}+{} == {}".format(args.x, args.y, args.bias, answer))
        else:
            print("{}^{} == {}".format(args.x, args.y, answer))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="calculate X to the power of Y, then add a bias if you like")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-v", "--verbose", action="store_true")
    group.add_argument("-q", "--quiet", action="store_true")

    parser.add_argument("x", type=int, help="the base")
    parser.add_argument("y", type=int, help="the exponent")

    parser.add_argument("-b", "--bias", type=int, help="the bias")

    main(parser.parse_args())


