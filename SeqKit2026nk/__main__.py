from SeqKit2026nk.logger import setup_logging
from SeqKit2026nk.modules import user_string_to_genbank

def main():
    setup_logging()
    user_string_to_genbank.main()

if __name__ == "__main__":
    main()