if __name__ == '__main__':
    try:
        import module1
        import module2

        module1.main()
        module2.main()
    except ImportError as error:
        print "You don't have module {0} installed".format(error.message[16:])
