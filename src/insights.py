from .jobs import read


def get_unique_job_types(path):
    complete_document = read(path)
    types_of_job = set()
    for row in complete_document:
        types_of_job.add(row["job_type"])
    return list(types_of_job)


def filter_by_job_type(jobs, job_type):
    job_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            job_list.append(job)
    return job_list


def get_unique_industries(path):
    complete_document = read(path)
    types_of_industries = set()
    for row in complete_document:
        if row["industry"] != "":
            types_of_industries.add(row["industry"])
    return list(types_of_industries)


def filter_by_industry(jobs, industry):
    industries_list = []
    for job in jobs:
        if job["industry"] == industry:
            industries_list.append(job)
    return industries_list


def get_max_salary(path):
    complete_document = read(path)
    salaries = list()
    for row in complete_document:
        if row["max_salary"].isdigit():
            new_salary = int(row["max_salary"])
            salaries.append(new_salary)
    return max(salaries)


def get_min_salary(path):
    complete_document = read(path)
    salaries = list()
    for row in complete_document:
        if row["min_salary"].isdigit():
            new_salary = int(row["min_salary"])
            salaries.append(new_salary)
    return min(salaries)


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
        or type(salary) is not int
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError
    if job["min_salary"] <= salary <= job["max_salary"]:
        return True
    else:
        return False


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
