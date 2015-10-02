import goslate
import sys

def main():
    try:
        text = ""
        target_language_code = ""
        gs = goslate.Goslate()
        language_code_dict = gs.get_languages()
        arg_count = len(sys.argv)
        
        if arg_count == 1:
            text = raw_input('Enter the text to be translated-:\n')
            target_language_code = raw_input('Enter the target language code-:\n')
        elif arg_count == 2:
            option = sys.argv[1]
            if option == '-lang':
                for index, mapping in enumerate(language_code_dict.iteritems(), start = 1):
                    print "{0}. {1} : {2}".format(index, mapping[1], mapping[0])
            else:
                usage = "'" + sys.argv[0] + " -lang' : List all the available languages with their codes\n"
                usage += "'" + sys.argv[0] + " <target_language_code> <text>' : Convert text to target language"
                print "Invalid option - '" + sys.argv[1] + "'"
                print "Usage -:"
                print usage
            return
        else:
            target_language_code = sys.argv[1]
            text = sys.argv[2]
        
        # If the input text is empty
        if not text:
            error_message = "Input text empty!!"
            raise Exception(error_message)
        if target_language_code not in language_code_dict:
            error_message = "Unknown language code - '" + target_language_code + "'"
            raise Exception(error_message)
        
        print gs.translate(text, target_language_code)
    except BaseException as exception:
        print "Error : {exception}".format(exception=exception.message)

if __name__ == '__main__':
    main()
