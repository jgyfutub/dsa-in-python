def createGraph(projects, dependencies):
    projectGraph = {}
    for project in projects:
        projectGraph[project] = []
    for pairs in dependencies:
        projectGraph[pairs[0]].extend(pairs[1])
    return projectGraph

project = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a','d'), ('f','b'), ('b','d'), ('f','a'), ('d','c')]

def getprojectWithDependencies(graph):
    projectWithDependencies=set()
    for project in graph:
        projectWithDependencies=projectWithDependencies.union(set(graph[project]))
    return projectWithDependencies

def getprojectWODependecies(projectWD, graph):
    projectsWODependecies=set()
    for project in graph:
        if not project in projectWD:
            projectsWODependecies.add(project)
    return projectsWODependecies

def findBuildOrder(projects,dependencies):
    buildOrder=[]
    projectGraph=createGraph(projects,dependencies)
    while projectGraph:
        projectWithDependencies=getprojectWithDependencies(projectGraph)
        projectWODependencies=getprojectWODependecies(projectWithDependencies,projectGraph)
        if len(projectWODependencies)==0 and projectGraph:
            raise ValueError("Cycle in order")
        for independentProjects in projectWODependencies:
            buildOrder.append(independentProjects)
            del projectGraph[independentProjects]
        return buildOrder
