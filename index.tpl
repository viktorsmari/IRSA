<html>
<head>
	<title>Verk2</title>
	<link rel="stylesheet" type="text/css" href="static/bootstrap.css">
	<script type="text/javascript" src="static/jquery.js"></script>
	<script type="text/javascript" src="static/bootstrap.min.js"></script>
</head>
<body>
	<div class="container">

		<!-- Top -->
		<div class="row">
			<div class="col-md-6 col-xs-6">
				<ul class="list-inline">

					%setdefault('notstarted',29)
					%setdefault('inprogress',28)
					%setdefault('waiting',27)
					%setdefault('ready',26)

				    <li>New: <strong>{{notstarted}}</strong></li>
				    <li>In progress: <strong> {{ inprogress }} </strong></li>
				    <li>Waiting: <strong> {{ waiting }} </strong></li>
				    <li>Ready: <strong> {{ ready }} </strong></li>
				</ul>
			</div>
			<div class="col-md-5 col-xs-5">
				<div class="input-group">
				  <span class="input-group-addon">?</span>
				  <input type="text" class="form-control" placeholder="Search">
				</div>
			</div>
			<div class="col-md-1 col-xs-1">
				<a href="">Log Out</a>
			</div>
		</div> <!-- end row Top -->

		<hr>

		<!-- Menu -->
		<div class="row">
			<div class="btn-group btn-group-lg">
				<a href="create" class="btn btn-default">Create</a>
				<a href="overview" class="btn btn-default">Overview</a>
				<a href="clients" class="btn btn-default">Clients</a>
				<a href="users" class="btn btn-default">Users</a>
				<a href="settings" class="btn btn-danger" >Settings</a>
			</div>
		</div> <!-- End row menu -->


		<!--  Should we INJECT stuff here? -->
		<!-- Instead of importing this file into every other files -->

	<!-- Rest is in footer.tpl -->