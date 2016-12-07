#!/usr/bin/env python

from subprocess import call

def main():
        call(["service", "nginx", "stop"])
        call(["/home/fox/letsencrypt/certbot-auto", "renew", "--quiet", "--no-self-upgrade"])
        call(["service", "nginx", "start"])

if __name__ == '__main__':
        main()
