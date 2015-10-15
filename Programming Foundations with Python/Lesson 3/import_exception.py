## http://stackoverflow.com/a/1618880/1815624
## https://docs.python.org/2/library/__main__.html
## https://docs.python.org/3/library/exceptions.html
if __name__ == '__main__':
    try:
        import donothavethis
        import orthat

        donothavethis.main()
        orthat.main()
    except ImportError as error:
        print(error)

