def paginate(items, page_size, current_page):
    total_items = len(items)
    total_pages = (total_items + page_size - 1) // page_size  # Ceiling division

    if current_page < 1 or current_page > total_pages:
        return f"Invalid page number. Must be between 1 and {total_pages}"

    start_index = (current_page - 1) * page_size
    end_index = min(start_index + page_size, total_items)

    page_items = items[start_index:end_index]

    return {
        "current_page": current_page,
        "total_pages": total_pages,
        "items_on_page": page_items
    }


# Example usage
items = [f"Item {i}" for i in range(1, 54)]  # 53 items
page_size = 10
current_page = 3  # You can change this

result = paginate(items, page_size, current_page)

if isinstance(result, str):
    print(result)
else:
    print(f"Showing page {result['current_page']} of {result['total_pages']}")
    for item in result['items_on_page']:
        print(item)
