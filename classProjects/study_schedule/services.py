def schedule_generate(selected_days, topics_raw):
    
    topics = [t.strip() for t in topics_raw.split(',')]
    days = [d.strip() for d in selected_days]

    schedule = {}
    i = 0
    for topic in topics:
        day = days[i % len(days)]
        if day in schedule:
            schedule[day].append(topic)
        else:
            schedule[day] = [topic]
        i += 1

    week_order = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
    ordered_schedule = {day: schedule.get(day, []) for day in week_order if day in schedule}

    return ordered_schedule