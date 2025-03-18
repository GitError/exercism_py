from lasagna.lasagna import elapsed_time_in_minutes

def main():
    layer_data = (1, 2, 5, 8, 11, 15)
    time_data = (3, 7, 8, 4, 15, 20)
    result_data = [5, 11, 18, 20, 37, 50]
    for variant, (layers, time, expected) in enumerate(zip(layer_data, time_data, result_data), start=1):
        result = elapsed_time_in_minutes(layers, time)
        print(f"Variant {variant}: {result} == {expected} -> {result == expected}")


if __name__ == "__main__":
    main()
