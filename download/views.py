from django.shortcuts import render
# Celery Task
from .tasks import ProcessDownload

def demo_view(request):
	# If method is POST, process form data and start task
	if request.method == 'POST':
		# Create Task
		download_task = ProcessDownload.delay()
		# Get ID
		task_id = download_task.task_id
		# Print Task ID
		print(f'Celery Task ID: {task_id}')
		# Return demo view with Task ID
		return render(request, 'progress.html', {'task_id': task_id})
	else:
		# Return demo view
		return render(request, 'progress.html', {})