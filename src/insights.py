from src.jobs import read


def get_unique_job_types(path):
    jobs_list = read(path)
    unique_job_types = []

    for job in jobs_list:
        if job["job_type"] not in unique_job_types:
            unique_job_types.append(job["job_type"])
    return unique_job_types


def filter_by_job_type(jobs, job_type):
    filtered_by_job_type = []
    for job in jobs:
        if job["job_type"] == job_type:
            filtered_by_job_type.append(job)
    return filtered_by_job_type


def get_unique_industries(path):
    jobs_list = read(path)
    unique_industries = []

    for job in jobs_list:
        item = job["industry"]
        if item not in unique_industries and len(item) != 0:
            unique_industries.append(item)
    return unique_industries


def filter_by_industry(jobs, industry):
    filtered_by_industry = []
    for job in jobs:
        if job["industry"] == industry:
            filtered_by_industry.append(job)
    return filtered_by_industry


def get_max_salary(path):
    jobs_list = read(path)
    max_salary = 0

    for job in jobs_list:
        if job["max_salary"].isdigit():
            current_value = int(job["max_salary"])
            if current_value > max_salary:
                max_salary = current_value
    return max_salary


def get_min_salary(path):
    jobs_list = read(path)
    new_salary_list = []

    for job in jobs_list:
        if job["min_salary"].isdigit():
            new_salary_list.append(int(job["min_salary"]))

    new_salary_list.sort()

    return new_salary_list[0]


def matches_salary_range(job, salary):
    if ('min_salary' or 'max_salary') not in job:
        raise ValueError('some value is missing')
    if type(job['min_salary'] or job['min_salary']) != int:
        raise ValueError('job values are not integer')
    if type(salary) != int:
        raise ValueError('salary is not integer')
    if job['min_salary'] > job['max_salary']:
        raise ValueError('min_salary is higher than max_salary')
    return job['min_salary'] <= salary <= job['max_salary']


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
