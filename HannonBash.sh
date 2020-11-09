#!/bin/bash

function discord-text-channel-download
{
   dotnet /home/matball/Projects/HannonDiscordChatExporter/DiscordChatExporter.Cli.dll export -t   NTkzNzU2MTk0NDM5NjkyMzAw.X6RG0w.CMSNbqjw_rY04vdOlSgff9PdxbQ -c "$1"
}

function discord-download-niemieckie-slowka
{
  discord-text-channel-download "705327376086728766"
}
