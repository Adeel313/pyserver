 #include "easywsclient.hpp"
#include "easywsclient.cpp" // <-- include only if you don't want compile separately
#ifdef _WIN32
#pragma comment( lib, "ws2_32" )
#include <WinSock2.h>
#endif
#include <cstdlib>
#include <assert.h>
#include <stdio.h>
#include <string>
#include <ctime>
using easywsclient::WebSocket;

static WebSocket::pointer ws = NULL;

void handle_message(const std::string & message)
{
    printf(">>> %s\n", message.c_str());
    if (message == "world") { ws->close(); }
}

int main()
{
#ifdef _WIN32
    INT rc;
    WSADATA wsaData;

    rc = WSAStartup(MAKEWORD(2, 2), &wsaData);
    if (rc) {
        printf("WSAStartup Failed.\n");
        return 1;
    }
#endif
    srand(time(0));
    ws = WebSocket::from_url("ws://localhost:5555/foo");
    assert(ws);

   // ws->send("hello");
    while (ws->getReadyState() != WebSocket::CLOSED) {
      ws->poll();
      ws->dispatch(handle_message);
      sleep(1);
    ws->send(std::to_string(rand() % 100));    }
    delete ws;
#ifdef _WIN32
    WSACleanup();
#endif
    return 0;
}
