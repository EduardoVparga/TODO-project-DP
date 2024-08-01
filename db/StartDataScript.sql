SELECT
	task.Id,
	Title,
	Datetime,
	Message,
	"User",
	Guess,
	Alarm,
	location.Name AS Location,
	priority.Priority AS Priority
FROM task
JOIN location 
ON task.LocationId = location.Id 
JOIN priority 
ON task.PriorityId = priority.Id