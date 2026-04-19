def square_matrix_simple(matrix=[]):
    # Yeni bir matris yaradırıq
    # Hər bir 'row' (sətir) üçün yeni list yaradılır və içindəki elementlər kvadrat yüksəldilir
    return [[x**2 for x in row] for row in matrix]
