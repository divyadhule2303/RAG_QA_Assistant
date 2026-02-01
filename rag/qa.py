def generate_answer(indices, chunks, sources):

    if not indices:
        return "Not found in documents.", []

    answer = ""
    used_sources = set()

    for i in indices:
        answer += chunks[i][:400] + "\n\n"
        used_sources.add(sources[i])

    return answer, list(used_sources)
