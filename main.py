from utils import get_data, get_filtered_data, get_final_list, get_last_value

def main():
    data = get_data()
    data = get_filtered_data(data)
    data = get_last_value(data)
    data = get_final_list(data)

if __name__ == "__main__":
    main()