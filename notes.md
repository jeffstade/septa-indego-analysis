# MUSA509 Final Project scratch pad

## Remaining ToDos

- [X] Set up airflow
- [ ] Set up scripts to run on airflow (https://github.com/musa-509-fall-2021/lab-07-airflow-in-the-cloud)
- [X] Add remaining bus and indego data to overview map
- [X] Add statistics to overview
- [X] Try in ipython narrowing down all station data geopandas df to just indego stations
- [X] Write a loop to create a station page for each Indego station
- [X] Fix DAG - templates folder not found, update route to template folder
- [X] Create individual station query (want to get all stops that are on a different service or line than the current one)
- [X] Create individual station pages (show a map of the station, all nearby stations on a different line within a 5 minute walk, added value of linking bikes)
- [X] Uncomment the upload to gcs line in render report, and the lines in transform data
- [ ] Add a bar chart to individual station page
- [ ] Figure out how to get summary statistics, probably rework query

/// example jinja

        <!--
        <p>
        The course "{{course.title}}" meets 
            {% if course.is_virtual %}
                virtually
            {% else %}
                in room {{course.room}}
            {% endif %}
        </p>

        <h2> Instructor </h2>
        <p>
            {{ course.instructor_name }}
        </p>

        <h2> Students</h2>
        <ul>
        {% for student_name in course.student_names %}
        <li>
            {{ student_name }}
        </li>
        {% endfor %}
    -->
