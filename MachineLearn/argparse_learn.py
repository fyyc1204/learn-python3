import argparse

parse = argparse.ArgumentParser()
parse.add_argument('-c','-console')
parse.add_argument('-e','-eonsole')
parse.add_argument('-d','-donsole')

args = parse.parse_args()
print(args)
# if(args.list):
#     print("1")
